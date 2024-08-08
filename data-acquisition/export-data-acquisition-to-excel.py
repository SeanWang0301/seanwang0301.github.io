import json
import pandas as pd

with open('data_acquisition.json') as f:
    data_acquisition = json.load(f)['data-acquisition']


df = pd.DataFrame(data_acquisition)

column_mapping = {
    "instrumentations.tag": "位号",
    "assets.description": "描述",
    "assets.serial_number": "序列号",
    "instrumentations.specifications.eh.user_config.medium_type.value": "类型",
    "instrumentations.description": "位置",
    "assets.specifications.eh.pcps.tmp.ordercode": "型号",
    "instrumentations.criticality": "级别",
    "assets.status.description": "状态",
    "assets.production_date": "生产日期",
    "assets.product.status.name": "工厂产品状态",
    "assets.product.order_stop_date": "订单停止日期",
    "assets.product.spare_parts_until": "备件停止日期"
}

df = df.rename(columns=column_mapping)
df['使用年限'] = 2024 - pd.to_datetime(df['生产日期'], errors = 'coerce').dt.year
df.to_excel('data-acquisition.xlsx', index=False)
print('Data acquisition has been exported to Excel successfully.')