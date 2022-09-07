/*
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
*/

/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function (s, t) {
  // Order must be preserved, therefore we must map as we go.
  // Example
  // PAPTER -> TITLE
  // Itter 1: p   t => taper
  // Itter 2: a   i => tiper
  // Itter 3: p in map => titer
  // Itter 4: e: l   l => titlr
  // Itter 5: r: e   t => title
  // if newS ==? t

  if (s === t) return true;

  let s_set = new Set(s.split(''));
  let t_set = new Set(t.split(''));

  if (s_set.size !== t_set.size) return false;

  let letterMap = {};

  for (let i = 0; i < s.length; i++) {
    //  is theletter already mapped.
    if (letterMap.hasOwnProperty(s[i])) {
      //  Does that equal the letter on 2nd array?
      if (letterMap[s[i]] !== t[i]) {
        return false;
      }
    } else {
      letterMap[s[i]] = t[i];
    }
  }
  return true;
};
