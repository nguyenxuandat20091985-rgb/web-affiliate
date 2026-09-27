import json, os
from datetime import datetime, timezone
import urllib.request

TODAY=datetime.now(timezone.utc).strftime("%Y-%m-%d")
products=[p.strip() for p in os.getenv("PRODUCT_URLS","").split(",") if p.strip()]
token=os.getenv("ACCESSTRADE_API_KEY","").strip()

def affiliate_link(url):
    if not token:
        return url
    try:
        req=urllib.request.Request(
            "https://api.accesstrade.vn/v1/custom_links",
            data=json.dumps({"url":url}).encode(),
            headers={"Authorization":f"Token {token}","Content-Type":"application/json"},
            method="POST")
        with urllib.request.urlopen(req,timeout=15) as resp:
            data=json.loads(resp.read().decode())
            return data.get("data",{}).get("short_link") or url
    except Exception:
        return url

items=[]
for i,url in enumerate(products[:10],1):
    items.append({
        "type":"affiliate",
        "title":f"Deal đáng xem #{i}",
        "url":affiliate_link(url),
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
print("Generated",TODAY,"items:",len(items),"affiliate:",bool(token))
