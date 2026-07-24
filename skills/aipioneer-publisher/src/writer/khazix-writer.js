/**
 * 卡兹克 (Khazix) 写作风格
 *
 * 特点：
 * - 活人感写作，像跟朋友聊天
 * - 从真实场景切入
 * - 口语化表达
 * - 长短句交替，节奏感强
 * - 文化升维
 */

class KhazixWriter {
  async rewrite(content) {
    const { title, text, author } = content;

    // 生成文章结构
    const article = {
      title: this.generateTitle(title),
      author: 'AI Pioneer',
      sections: this.parseSections(text),
      originalAuthor: author
    };

    return article;
  }

  generateTitle(originalTitle) {
    // 简化标题，去掉英文，保留核心意思
    if (!originalTitle) return '未命名文章';

    // 如果标题已经很短，直接返回
    if (originalTitle.length < 20) return originalTitle;

    // 提取核心关键词
    return originalTitle
      .replace(/Resolvers?/g, 'Resolver')
      .replace(/Claude Skills?/g, 'Claude Skills')
      .substring(0, 30);
  }

  parseSections(text) {
    // 将长文本分段
    const paragraphs = text.split('\n').filter(p => p.trim());

    // 提取核心观点作为章节
    const sections = [];
    let currentSection = {
      number: '01',
      title: '核心观点',
      content: []
    };

    for (const para of paragraphs.slice(0, 20)) {
      if (para.length > 50) {
        currentSection.content.push(para.trim());
      }
    }

    sections.push(currentSection);

    // 添加总结章节
    sections.push({
      number: '02',
      title: '写在最后',
      content: ['这篇文章的核心观点值得深思。你怎么看？评论区聊聊。']
    });

    return sections;
  }
}

module.exports = new KhazixWriter();