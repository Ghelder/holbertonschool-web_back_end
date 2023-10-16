export default function cleanSet(set, startString) {
  if (!startString) {
    return '';
  }

  return Array.from(set)
    .filter((parametro) => parametro && parametro.startsWith(startString))
    .map((parametro) => parametro.slice(startString.length))
    .join('-');
}
