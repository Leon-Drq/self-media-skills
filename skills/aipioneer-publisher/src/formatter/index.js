/**
 * 排版样式模块
 */

const aiPioneerBlack = require('./ai-pioneer-style');

const styles = {
  'ai-pioneer-black': aiPioneerBlack
};

/**
 * 格式化文章
 * @param {Object} article - 文章对象
 * @param {string} styleName - 样式名称
 */
function format(article, styleName = 'ai-pioneer-black') {
  const style = styles[styleName];
  if (!style) {
    throw new Error(`未知的样式: ${styleName}`);
  }

  let html = '';

  // 标签
  html += `<p style="margin:0 0 10px;">${style.components.tag('AI Pioneer · 精选')}</p>\n`;

  // 章节
  for (const section of article.sections) {
    // 章节标题
    html += style.components.sectionTitle(section.number, section.title);

    // 内容段落
    for (const content of section.content) {
      // 简单处理：长句拆分段落
      const paragraphs = this.splitParagraphs(content);
      for (const para of paragraphs) {
        html += style.components.paragraph(para);
      }
    }
  }

  // 结尾
  html += style.components.footer();

  return html;
}

/**
 * 拆分长段落
 */
function splitParagraphs(text) {
  // 按句号拆分，每 2-3 句一段
  const sentences = text.split(/([。！？])/);
  const paragraphs = [];
  let current = '';

  for (let i = 0; i < sentences.length; i += 2) {
    current += sentences[i];
    if (sentences[i + 1]) current += sentences[i + 1];

    if (current.length > 100 || i >= sentences.length - 2) {
      paragraphs.push(current.trim());
      current = '';
    }
  }

  if (current.trim()) {
    paragraphs.push(current.trim());
  }

  return paragraphs.length > 0 ? paragraphs : [text];
}

module.exports = {
  format: (article, style) => format(article, style)
};