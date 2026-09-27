import fs from "node:fs";

const catalog = JSON.parse(fs.readFileSync("ai-50k/products.json", "utf8"));
const products = Array.isArray(catalog.products) ? catalog.products : [];
const date = new Date().toISOString().slice(0, 10);
const day = Number(date.slice(-2)) || 1;
const start = products.length ? (day * 3) % products.length : 0;
const picked = Array.from({length: Math.min(10, products.length)}, (_, i) => products[(start + i) % products.length]);

const out = {
  id: "ai50k-" + date.replaceAll("-", ""),
  date,
  target_vnd: 50000,
  status: "ready",
  note: "AI chạy theo catalog. Doanh thu chỉ ghi nhận khi có giao dịch/hoa hồng thực tế.",
  items: picked.map(p => ({type: "affiliate", title: p.name, url: p.url, cta: "Xem sản phẩm"}))
};

fs.writeFileSync("ai-50k/daily/latest.json", JSON.stringify(out, null, 2) + "\n");
