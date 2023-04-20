const formatChangeString = (change, percent) => {
  if (change === null || percent === null) return null;
  const op = Number(change) >= 0 ? `+` : "";
  return `${op}${change} (${op}${percent}%)`;
};

const formatTwoDecimalPlaces = (num) => {
  if (num === null) return null;
  return Number.parseFloat(num).toFixed(2);
};

const formatLargeNumbers = (num) => {
  if (num === null) return null;

  const trillion = 1000000000000;
  if (num / trillion > 1) {
    return `${(num / trillion).toFixed(3)}T`;
  }
  if (num / (trillion / 1000) > 1) {
    return `${(num / (trillion / 1000)).toFixed(2)}B`;
  }
  return `${(num / (trillion / 1000000)).toFixed(2)}M`;
};

export { formatChangeString, formatTwoDecimalPlaces, formatLargeNumbers };
