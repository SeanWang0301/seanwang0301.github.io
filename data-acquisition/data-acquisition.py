import json

with open('instrumentations.json') as f:
    instrumentations = json.load(f)

with open('assets.json') as f:
    assets = json.load(f)


assets_dict = {asset['id']: asset for asset in assets['assets']}

data_acquisition = []

for instrumentation in instrumentations['instrumentations']:
    for asset_ref in instrumentation['assets']:
        asset_id = asset_ref['id']
        asset = assets_dict.get(asset_id, {})

        data_entry = {
            "instrumentations.tag": instrumentation.get("tag", ""),
            "instrumentations.description": instrumentation.get("description", ""),
            "instrumentations.criticality": instrumentation.get("criticality", ""),
            "instrumentations.specifications.eh.user_config.medium_type.value": instrumentation.get("specifications", {}).get("eh.user_config.medium_type", {}).get("value", ""),
            "instrumentations.assets_id": asset_id,
            "assets.serial_number": asset.get("serial_number", ""),
            "assets.description": asset.get("description", ""),
            "assets.status.description": asset.get("status", ()).get("description", ""),
            "assets.production_date": asset.get("production_date", ""),
            "assets.product.status.name": asset.get("product", {}).get("status", {}).get("name", ""),
            "assets.product.order_stop_date": asset.get("product", {}).get("order_stop_date", ""),
            "assets.product.spare_parts_until": asset.get("product", {}).get("spare_parts_until"),
            "assets.specifications.eh.pcps.tmp.ordercode": asset.get("specifications", {}).get("eh.pcps.tmp.ordercode", {}).get("value", "")
        }

        data_acquisition.append(data_entry)

final_output = {
    "data-acquisition": data_acquisition
}

with open('data_acquisition.json', 'w') as f:
    json.dump(final_output, f, ensure_ascii=False, indent=4)

print("Data acquisition JSON has been created successfully.")