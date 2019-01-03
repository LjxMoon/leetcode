/**
 * @param {number} x
 * @return {number}
 */
var reverse = function (x) {
  const sign = x < 0
  const num = Math.abs(x).toString()
  const numList = num.split('')
  let ans = parseInt((numList.reverse()).join(''))
  if (sign) {
    ans = -ans
  }
  const maxNum = Math.pow(2, 31) - 1
  const minNum = -Math.pow(2, 31)
  if (ans >= maxNum || ans <= minNum) {
    return 0
  }
  return ans
};