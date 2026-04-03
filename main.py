# 任务 1.0 变量、数据类型、输入输出
#个人记账工具V 1.0
print("=" * 30)
print("个人记账工具 v1.0")
print("=" * 30)
# 变量与输入
amount = input("请输入金额：")
note = input("请输入备注：")
# 数据类型转换
amount = float(amount)
# 输出结果
print(f"已记录：{note}, 金额：{amount:.2f}元")
print(f"当前余额：{amount:.2f}元") #简化版