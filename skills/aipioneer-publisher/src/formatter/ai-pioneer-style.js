/**
 * AI Pioneer 纯黑样式
 *
 * 特点：
 * - 黑底白字标签
 * - 80px 大号章节数字
 * - 纯黑强调文字
 * - 极简高级感
 */

const AI_PIONEER_BLACK = {
  name: 'ai-pioneer-black',
  colors: {
    primary: '#000000',
    text: '#333333',
    background: '#ffffff',
    accent: '#000000',
    quote: 'rgba(0,0,0,0.06)',
    light: 'rgba(0,0,0,0.08)'
  },
  fonts: {
    family: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', 'PingFang SC', 'Microsoft YaHei', sans-serif",
    bodySize: '16px',
    headingSize: '24px',
    numberSize: '80px',
    lineHeight: '2.0'
  },
  components: {
    // 标签样式
    tag: (text) => `
      <span style="display:inline-block;background:#000000;color:#ffffff;font-size:11px;padding:3px 12px;border-radius:20px;letter-spacing:1.5px;">
        ${text}
      </span>
    `,

    // 章节标题样式
    sectionTitle: (number, title) => `
      <p style="margin:0 0 8px;">
        <span style="display:block;font-size:80px;font-weight:700;color:rgba(0,0,0,0.08);line-height:1;letter-spacing:-2px;">${number}</span>
        <span style="display:block;font-size:24px;font-weight:700;color:#000000;line-height:1.3;margin-top:-48px;">${title}</span>
      </p>
    `,

    // 正文段落
    paragraph: (text) => `
      <p style="font-size:16px;color:#333;line-height:2.0;margin:0 0 16px;">${text}</p>
    `,

    // 强调文字
    strong: (text) => `
      <strong style="color:#000000;">${text}</strong>
    `,

    // 引用块
    quote: (text) => `
      <p style="font-size:16px;color:#000000;font-weight:700;line-height:2.0;margin:0 0 16px;padding:10px 16px;background:rgba(0,0,0,0.06);border-radius:8px;">
        ${text}
      </p>
    `,

    // 结尾引导
    footer: () => `
      <p style="border-top:1px solid rgba(0,0,0,0.1);margin:0;"><br></p>
      <p style="margin:0;padding:24px 0;text-align:center;">
        <strong style="font-size:16px;color:#333;display:block;margin-bottom:10px;">觉得有用？</strong>
        <span style="font-size:14px;color:#666;line-height:1.8;display:block;margin-bottom:16px;">点个<span style="color:#000000;">❤️</span><strong style="color:#000000;">在看</strong>，转给还不知道的朋友</span>
        <span style="font-size:14px;color:#666;line-height:2;display:block;">关注「AI Pioneer」，下次更新第一时间收到</span>
      </p>
    `
  }
};

module.exports = AI_PIONEER_BLACK;