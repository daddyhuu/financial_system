import pymysql
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 数据库连接配置
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '011001',
    'database': 'stresstesting',
    'charset': 'utf8mb4'
}

# 从数据库中获取公司数据
def get_companies_from_db(query_string, table_name):
    connection = pymysql.connect(**db_config)
    try:
        with connection.cursor() as cursor:
            sql = f"SELECT DISTINCT `company` FROM `{table_name}` WHERE LOWER(`company`) LIKE %s"
            cursor.execute(sql, ('%' + query_string.lower() + '%',))
            result = cursor.fetchall()
            return [row[0] for row in result]
    finally:
        connection.close()

@app.route('/interest_rate_risk/search', methods=['GET'])
def interest_rate_risk_search():
    query_string = request.args.get('company', '')
    companies = get_companies_from_db(query_string, 'interest_rate_risk')
    if not companies:
        return jsonify({"message": "公司名称不存在"}), 404
    return jsonify(companies)

@app.route('/interest_rate_risk/test', methods=['POST'])
def interest_rate_risk_test():
    data = request.json
    # 检查数据是否包含公司名称和情景
    if data and 'company' in data and 'scenario' in data:
        company_name = data['company']
        scenario = data['scenario']
        # 从数据库中获取每年数据
        connection = pymysql.connect(**db_config)
        try:
            with connection.cursor() as cursor:
                sql = """
                SELECT `year`, `gap1`, `gap2`, `gap3`, `gap4`
                FROM `interest_rate_risk`
                WHERE `company` = %s
                """
                cursor.execute(sql, (company_name,))
                result = cursor.fetchall()
                
                # 计算加权结果并乘以情景值
                weights = [0.125, 0.625, 3, 6]
                weighted_results = []
                for row in result:
                    year, gap1, gap2, gap3, gap4 = row
                    weighted_sum = (gap1 * weights[0] + gap2 * weights[1] + gap3 * weights[2] + gap4 * weights[3]) * scenario
                    weighted_results.append({'year': year, 'weighted_sum': weighted_sum})
                
                return jsonify(weighted_results)
        finally:
            connection.close()
    else:
        return jsonify({"message": "测试出现问题"}), 400

@app.route('/currency_risk/search', methods=['GET'])
def currency_risk_search():
    query_string = request.args.get('company', '')
    companies = get_companies_from_db(query_string, 'currency_risk')
    if not companies:
        return jsonify({"message": "公司名称不存在"}), 404
    return jsonify(companies)

@app.route('/currency_risk/test', methods=['POST'])
def currency_risk_test():
    data = request.json
    # 检查数据是否包含公司名称和情景
    if data and 'company' in data and 'scenario' in data:
        company_name = data['company']
        scenario = data['scenario']
        # 从数据库中获取每年数据
        connection = pymysql.connect(**db_config)
        try:
            with connection.cursor() as cursor:
                sql = """
                SELECT `year`, `USD`, `HKD`, `other`
                FROM `currency_risk`
                WHERE `company` = %s
                """
                cursor.execute(sql, (company_name,))
                result = cursor.fetchall()
                # 将每个汇率值乘以情景值
                results = []
                for row in result:
                    year, usd, hkd, other = row
                    results.append({
                        'year': year,
                        'weighted_sum': (usd + hkd + other) * scenario
                    })
                return jsonify(results)
        finally:
            connection.close()
    else:
        return jsonify({"message": "测试出现问题"}), 400

@app.route('/stock_price_risk/search', methods=['GET'])
def stock_price_risk_search():
    query_string = request.args.get('company', '')
    companies = get_companies_from_db(query_string, 'stock_price_risk')
    if not companies:
        return jsonify({"message": "公司名称不存在"}), 404
    return jsonify(companies)

@app.route('/stock_price_risk/test', methods=['POST'])
def stock_price_risk_test():
    data = request.json
    # 检查数据是否包含公司名称和情景
    if data and 'company' in data and 'scenario' in data:
        company_name = data['company']
        scenario = data['scenario']
        # 从数据库中获取每年数据
        connection = pymysql.connect(**db_config)
        try:
            with connection.cursor() as cursor:
                sql = """
                SELECT `year`, `invest1`, `invest2`, `invest3`
                FROM `stock_price_risk`
                WHERE `company` = %s
                """
                cursor.execute(sql, (company_name,))
                result = cursor.fetchall()
                # 将每个汇率值乘以情景值
                results = []
                for row in result:
                    year, invest1, invest2, invest3 = row
                    results.append({
                        'year': year,
                        'weighted_sum': (invest1 + invest2 + invest3) * scenario
                    })
                return jsonify(results)
        finally:
            connection.close()
    else:
        return jsonify({"message": "测试出现问题"}), 400   

# 智能利率风险压力情景更新
@app.route('/smart_interest_rate_risk', methods=['POST'])
def smart_interest_rate_risk():
    data = request.json
    if isinstance(data, dict) and 'scenarios' in data:
        scenarios = data['scenarios']
        # Shibor 的波动率为 0.10%
        Shibor = 0.001
        # 99%的置信水平下z值为2.58
        improve = Shibor * 2.58
        for scenario in scenarios:
            if scenario['value'] > 0:
                scenario['value'] += improve
            else:
                scenario['value'] -= improve
            # 更新 label
            scenario['label'] = f"{'上升' if scenario['value'] > 0 else '下降'}{abs(scenario['value'] * 100):.2f}%"
        return jsonify({'scenarios': scenarios})
    else:
        return jsonify({"message": "情景未正确传到后端"}), 400

# 智能汇率风险压力情景更新
@app.route('/smart_currency_risk', methods=['POST'])
def smart_currency_risk():
    data = request.json
    if isinstance(data, dict) and 'scenarios' in data:
        scenarios = data['scenarios']
        # 汇率的波动率为 3.4%
        p = 0.034
        # 99%的置信水平下z值为2.58
        improve = p * 2.58
        for scenario in scenarios:
            if scenario['value'] > 0:
                scenario['value'] += improve
            else:
                scenario['value'] -= improve
            # 更新 label
            scenario['label'] = f"{'外币升值' if scenario['value'] > 0 else '外币贬值'}{abs(scenario['value'] * 100):.2f}%"
        return jsonify({'scenarios': scenarios})
    else:
        return jsonify({"message": "情景未正确传到后端"}), 400

# 智能股票价格风险压力情景更新
@app.route('/smart_stock_price_risk', methods=['GET'])
def smart_stock_price_risk():
    # 上证指数收益率的标准差为 9.53%
    p = 0.0953
    # 99%的置信水平下z值为2.58
    base_value = p * 2.58
    # 定义新的情景值
    scenario_values = [0.75, 1.0, 1.25]
    scenarios = []
    for value in scenario_values:
        for sign in [1, -1]:
            adjusted_value = base_value * value * sign
            label = f"{'上升' if sign > 0 else '下降'}{abs(adjusted_value * 100):.2f}%"
            scenarios.append({'value': adjusted_value, 'label': label})
    # 先按正负排序，再按绝对值从小到大排序
    scenarios.sort(key=lambda x: (x['value'] < 0, abs(x['value'])))
    return jsonify({'scenarios': scenarios})

if __name__ == '__main__':
    app.run(debug=True)
