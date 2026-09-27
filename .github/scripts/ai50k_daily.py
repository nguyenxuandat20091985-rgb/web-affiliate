import json, os
from datetime import datetime, timezone

TODAY=datetime.now(timezone.utc).strftime("%Y-%m-%d")
products=[p.strip() for p in os.getenv("PRODUCT_URLS","").split(",") if p.strip()]

items=[]
for i,url in enumerate(products[:10],1):
    items.append({
        "type":"affiliate",
        "title":f"Deal đáng xem #{i}",
        "url":url,
        "cta":"Xem giá và thông tin sản phẩm"
    })

if not items:
    items=[{
        "type":"content",
        "title":"3 mẹo săn deal hôm nay",
        "url":"",
        "cta":"Xem bài và chọn sản phẩm phù hợp"
    }]

payload={
  "date":TODAY,
  "target_vnd":50000,
  "status":"ready",
  "note":"Doanh thu chỉ được ghi nhận khi có giao dịch/hoa hồng thực tế.",
  "items":items
}
os.makedirs("ai-50k/daily",exist_ok=True)
with open(f"ai-50k/daily/{TODAY}.json","w",encoding="utf-8") as f:
    json.dump(payload,f,ensure_ascii=False,indent=2)
with open("ai-50k/daily/latest.json","w",encoding="utf-8") as f:
    json.dump(payload,f,ensure_ascii=False,indent=2)
print("Generated", TODAY, "items:", len(items))
