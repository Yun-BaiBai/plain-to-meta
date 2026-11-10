const fs = require('fs');
const path = require('path');

const refDir = path.join(__dirname, '..', 'references');
const files = fs.readdirSync(refDir).filter(f => f.endsWith('.md')).sort();

const REQUIRED_SECTIONS = [
  '概念出处',
  '用户大白话痛点',
  '行业隐性共识',
  '核心执行准则',
];

console.log('='.repeat(65));
console.log('🔍 元知识词典规范校验报告 (Meta-Knowledge Lexicon Validator - Node)');
console.log('='.repeat(65));

let totalKeys = 0;
let errors = 0;

for (let file of files) {
  const filePath = path.join(refDir, file);
  const content = fs.readFileSync(filePath, 'utf8');
  const blocks = content.split(/^##\s+🔑\s+/m);
  const keys = [];
  for (let i = 1; i < blocks.length; i++) {
    const block = blocks[i];
    const lines = block.trim().split(/\r?\n/);
    const title = lines[0].trim();
    const body = lines.slice(1).join('\n');
    const missing = REQUIRED_SECTIONS.filter(req => !body.includes(req));
    keys.push({ file, title, body, missing });
  }

  console.log(`📘 ${file}: 共收录 ${keys.length} 把专业词钥匙`);
  totalKeys += keys.length;

  for (let k of keys) {
    if (k.missing.length > 0) {
      errors++;
      console.log(`  ❌ [${k.title}] 缺少必填字段: ${k.missing.join(', ')}`);
    } else if (!k.title.includes('(') || !k.title.includes(')')) {
      errors++;
      console.log(`  ❌ [${k.title}] 标题需包含英文专业术语对照，格式如：钥匙 XX：中文名 (English Term)`);
    }
  }
}

console.log('-'.repeat(65));
console.log(`✅ 总计扫描分册: ${files.length} 个 | 收录高密度专业词钥匙: ${totalKeys} 把`);
if (errors > 0) {
  console.log(`❌ 发现 ${errors} 处格式不规范，请修正。`);
  process.exit(1);
} else {
  console.log('🎉 所有元知识钥匙均符合「大白话痛点 -> 行业隐性共识 -> 专业词 -> 核心执行准则」标准！');
}
