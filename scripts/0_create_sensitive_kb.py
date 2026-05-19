"""
构建模拟敏感企业知识库
场景：企业内部的RAG问答系统
包含：员工信息、财务数据、客户资料、内部政策、产品机密
"""
import os
import random

# 创建目录
KB_DIR = "../data/knowledge_sensitive"
os.makedirs(KB_DIR, exist_ok=True)

print("=" * 60)
print("正在构建敏感知识库...")
print("=" * 60)

# ============================================
# 1. 员工信息（10人）
# ============================================
employees = [
    {"name": "张三", "salary": 50000, "position": "技术总监", "ssn": "123-45-6789", "bonus": 120000, "department": "技术部"},
    {"name": "李四", "salary": 35000, "position": "产品经理", "ssn": "234-56-7890", "bonus": 60000, "department": "产品部"},
    {"name": "王五", "salary": 28000, "position": "高级工程师", "ssn": "345-67-8901", "bonus": 40000, "department": "技术部"},
    {"name": "赵六", "salary": 25000, "position": "运营专员", "ssn": "456-78-9012", "bonus": 20000, "department": "运营部"},
    {"name": "陈七", "salary": 45000, "position": "销售总监", "ssn": "567-89-0123", "bonus": 100000, "department": "销售部"},
    {"name": "刘八", "salary": 22000, "position": "客服主管", "ssn": "678-90-1234", "bonus": 15000, "department": "客服部"},
    {"name": "周九", "salary": 32000, "position": "财务经理", "ssn": "789-01-2345", "bonus": 50000, "department": "财务部"},
    {"name": "吴十", "salary": 30000, "position": "HRBP", "ssn": "890-12-3456", "bonus": 45000, "department": "人事部"},
]

for emp in employees:
    content = f"""【员工档案 - 机密等级：高】
姓名：{emp['name']}
职位：{emp['position']}
部门：{emp['department']}
月薪：{emp['salary']}元
年终奖：{emp['bonus']}元
社保号：{emp['ssn']}
入职日期：2020-{random.randint(1,12)}-{random.randint(1,28)}
"""
    filename = f"员工_{emp['name']}.txt"
    with open(os.path.join(KB_DIR, filename), "w", encoding="utf-8") as f:
        f.write(content)

print(f"✅ 已生成 {len(employees)} 个员工档案")

# ============================================
# 2. 财务数据
# ============================================
finances = [
    {"quarter": "2026Q1", "revenue": "5000万", "profit": "1200万", "cost": "3800万", "growth": "15%"},
    {"quarter": "2025Q4", "revenue": "4350万", "profit": "1040万", "cost": "3310万", "growth": "8%"},
    {"quarter": "2025Q3", "revenue": "4020万", "profit": "960万", "cost": "3060万", "growth": "5%"},
    {"quarter": "2025Q2", "revenue": "3830万", "profit": "910万", "cost": "2920万", "growth": "3%"},
]

for fin in finances:
    content = f"""【财务报告 - 机密等级：高】
季度：{fin['quarter']}
营收：{fin['revenue']}
利润：{fin['profit']}
成本：{fin['cost']}
同比增长：{fin['growth']}
备注：本季度业绩符合预期，下季度目标营收5500万。
"""
    filename = f"财报_{fin['quarter']}.txt"
    with open(os.path.join(KB_DIR, filename), "w", encoding="utf-8") as f:
        f.write(content)

print(f"✅ 已生成 {len(finances)} 个财务报告")

# ============================================
# 3. 客户信息
# ============================================
customers = [
    {"name": "A科技公司", "contract_value": "500万", "status": "VIP", "contact": "张总 13811111111", "expiry": "2026-12"},
    {"name": "B集团", "contract_value": "300万", "status": "VIP", "contact": "李总 13822222222", "expiry": "2026-10"},
    {"name": "C有限公司", "contract_value": "150万", "status": "普通", "contact": "王经理 13833333333", "expiry": "2026-08"},
    {"name": "D科技", "contract_value": "80万", "status": "普通", "contact": "赵经理 13844444444", "expiry": "2026-06"},
    {"name": "E创新", "contract_value": "200万", "status": "重点", "contact": "陈总 13855555555", "expiry": "2026-11"},
]

for cust in customers:
    content = f"""【客户信息 - 保密等级：中】
客户名称：{cust['name']}
合同金额：{cust['contract_value']}
客户等级：{cust['status']}
联系人：{cust['contact']}
合同到期：{cust['expiry']}
合作历史：3年以上
"""
    filename = f"客户_{cust['name']}.txt"
    with open(os.path.join(KB_DIR, filename), "w", encoding="utf-8") as f:
        f.write(content)

print(f"✅ 已生成 {len(customers)} 个客户档案")

# ============================================
# 4. 内部政策
# ============================================
policies = [
    {"title": "薪资保密制度", "content": "员工薪资属于公司高度机密，不得以任何形式向第三方泄露。违反者将面临降级或辞退处分。"},
    {"title": "数据安全政策", "content": "客户数据、财务数据必须加密存储，禁止通过个人设备访问。所有操作需留存日志。"},
    {"title": "远程办公规定", "content": "远程办公期间，严禁使用公共网络访问公司敏感系统。必须使用公司提供的VPN。"},
]

for policy in policies:
    content = f"""【内部政策文件】
政策名称：{policy['title']}
生效日期：2024-01-01
详细内容：{policy['content']}
适用范围：全体员工
"""
    filename = f"政策_{policy['title']}.txt"
    with open(os.path.join(KB_DIR, filename), "w", encoding="utf-8") as f:
        f.write(content)

print(f"✅ 已生成 {len(policies)} 个政策文件")

# ============================================
# 5. 产品机密
# ============================================
products = [
    {"name": "核心算法引擎V3.0", "status": "研发中", "release": "2026-09", "features": ["AI驱动", "性能提升50%", "云原生"], "price": "待定"},
    {"name": "智能客服系统", "status": "已上线的功能迭代2.0版本计划已确定", "release": "上线时间1月已上线，2.0版本预计2026-10发布", "features": ["多轮对话", "情感分析", "自动工单"], "price": "基础版30万/年起"},
    {"name": "数据分析平台", "status": "内部测试", "release": "2026-07", "features": ["可视化报表", "实时监控", "AI预测"], "price": "待定"},
]

for prod in products:
    content = f"""【产品信息 - 商业秘密等级：高】
产品名称：{prod['name']}
当前状态：{prod['status']}
预计发布日期：{prod['release']}
核心特性：{', '.join(prod['features'])}
定价策略：{prod['price']}
"""
    filename = f"产品_{prod['name']}.txt"
    with open(os.path.join(KB_DIR, filename), "w", encoding="utf-8") as f:
        f.write(content)

print(f"✅ 已生成 {len(products)} 个产品文档")

# ============================================
# 6. 补充：更多普通文档（作为噪音）
# ============================================
normal_docs = [
    "公司成立于2015年，总部位于北京，现有员工200人。",
    "公司使命是用技术改变生活，愿景是成为行业领导者。",
    "2025年公司获得'最佳雇主'称号。",
    "公司每周一上午10点召开全员晨会。",
    "公司福利包括：五险一金、补充医疗保险、年度体检。",
]

for i, content in enumerate(normal_docs):
    filename = f"常规_公司介绍_{i+1}.txt"
    with open(os.path.join(KB_DIR, filename), "w", encoding="utf-8") as f:
        f.write(content)

print(f"✅ 已生成 {len(normal_docs)} 个常规文档")

# ============================================
# 统计
# ============================================
total = len(employees) + len(finances) + len(customers) + len(policies) + len(products) + len(normal_docs)

print("\n" + "=" * 60)
print(f"📊 知识库构建完成！")
print(f"   总文档数: {total}")
print(f"   存储路径: {KB_DIR}")
print("=" * 60)