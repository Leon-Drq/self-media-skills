/**
 * 写作风格模块
 * 支持多种写作风格改写
 */

const khazixWriter = require('./khazix-writer');

const writers = {
  khazix: khazixWriter
};

/**
 * 改写内容
 * @param {Object} content - 原始内容
 * @param {string} style - 写作风格
 */
async function rewrite(content, style = 'khazix') {
  const writer = writers[style];
  if (!writer) {
    throw new Error(`未知的写作风格: ${style}`);
  }

  return await writer.rewrite(content);
}

module.exports = {
  rewrite
};