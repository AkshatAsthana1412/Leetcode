### 🔁 Sliding Window — Recognize by These Clues

	•	You’re told to find:
	•	The maximum/minimum/longest/shortest subarray or substring satisfying a condition.
	•	A subarray whose sum, distinct count, or character frequency matches a requirement.

### ↔️ Two Pointer — Recognize by These Clues

	•	You’re told to:
	•	Find pairs or triplets that meet a numeric condition.
	•	Traverse two arrays (or the same array) to compare elements.
	•	Remove duplicates or partition elements based on some value.
	•	Common when:
	•	Array is sorted (or can be sorted).
	•	You’re comparing nums[i] + nums[j] or checking some relationship.
` you usually don’t track window state, just move pointers based on values. `

## 💡 Mnemonic to Remember

	•	“Window” = stateful region — you keep track of what’s inside.
	•	“Two pointers” = value comparison — you act based on array values, not what’s in between.