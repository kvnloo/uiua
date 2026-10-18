# Candidate reproduction for uiua-lang/uiua#1041
# A matched-needle case for comparison (present in the original haystack).
⍜⊗+0 "bab" "baa"

# Proposed identity behavior for an unmatched needle:
# expected under the requested semantics: "bac"
⍜⊗+0 "bab" "bac"

# A changed-position sentinel case; exact inverse semantics need agreement.
⍜⊗⇌ "bab" "bac"
