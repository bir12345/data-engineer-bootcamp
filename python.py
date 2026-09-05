def reverse_string(s):
    result = ""
    for ch in s:
        result = ch + result
    return result

print("Reverse string:", reverse_string("python"))

def first_non_repeating_char(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    for ch in s:
        if freq[ch] == 1:
            return ch
    return None
print("First non-repeating char:", first_non_repeating_char("programming"))

def is_palindrome(s):
    return s == reverse_string(s)
print("Palindrome check:", is_palindrome("madam"))

def char_frequency(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq
print("Char frequency:", char_frequency("hello"))

def remove_duplicate_chars(s):
    seen = set()
    result = ""
    for ch in s:
        if ch not in seen:
            seen.add(ch)
            result += ch
    return result
print("Remove duplicate chars:", remove_duplicate_chars("programming"))

def remove_duplicates_list(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result
print("Remove duplicates:", remove_duplicates_list([1, 2, 2, 3, 4, 4]))

def second_largest(lst):
    largest = second = float("-inf")
    for num in lst:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
    return second
print("Second largest:", second_largest([10, 20, 5, 30, 25])

def find_duplicates(lst):
    seen = set()
    duplicates = []
    for item in lst:
        if item in seen and item not in duplicates:
            duplicates.append(item)
        else:
            seen.add(item)
    return duplicates
print("Find duplicates:", find_duplicates([1, 2, 3, 2, 4, 5, 1]))

def rotate_list(lst, k):
    if not lst:
        return lst
    k = k % len(lst)
    return lst[k:] + lst[:k]
print("Rotate list by K=2:", rotate_list([1, 2, 3, 4, 5], 2))

def list_intersection(lst1, lst2):
    result = []
    lst2_copy = list(lst2)
    for item in lst1:
        if item in lst2_copy and item not in result:
            result.append(item)
    return result
print("List intersection:", list_intersection([1, 2, 3, 4], [3, 4, 5, 6]))

def count_frequency_dict(lst):
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    return freq
print("Count frequency:", count_frequency_dict([1, 2, 2, 3, 3, 3]))

def key_with_max_value(d):
    max_key = None
    max_val = float("-inf")
    for key, val in d.items():
        if val > max_val:
            max_val = val
            max_key = key
    return max_key
print("Key with max value:", key_with_max_value({"A": 100, "B": 500, "C": 300}))

def reverse_dict(d):
    return {value: key for key, value in d.items()}
print("Reverse dict:", reverse_dict({"a": 1, "b": 2}))

def merge_dicts(d1, d2):
    merged = d1.copy()
    merged.update(d2)
    return merged
print("Merge dicts:", merge_dicts({"a": 1}, {"b": 2}))

def word_frequency(sentence):
    words = sentence.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq
print("Word frequency:", word_frequency("python is good python is easy"))

def print_star_pattern(rows=5):
    for i in range(1, rows + 1):
            print("*" * i)
print_star_pattern(5)

def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
print("\nMultiplication table of 5:")
multiplication_table(5)

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print("\n Factorial of 5:", factorial(5))

def primes_up_to_100():
    primes = []
    for num in range(2, 101):
        is_prime = True
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes
print("Primes up to 100:", primes_up_to_100())

def fibonacci_series(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series
print("Fibonacci (8 terms):", fibonacci_series(8))

def first_non_repeating_number(lst):
    freq = {}
    for num in lst:
        freq[num] = freq.get(num, 0) + 1
    for num in lst:
        if freq[num] == 1:
            return num
    return None
print("First non-repeating number:",first_non_repeating_number([1, 2, 3, 4, 5, 1, 2, 3]))

def nth_non_repeating_number(lst, n):
    freq = {}
    for num in lst:
        freq[num] = freq.get(num, 0) + 1
    non_repeating = [num for num in lst if freq[num] == 1]
    if n <= len(non_repeating):
        return non_repeating[n - 1]
    return None
print("2nd non-repeating number:", nth_non_repeating_number([1, 2, 3, 4, 5, 1, 2, 3], 2))

def are_anagrams(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    return sorted(s1) == sorted(s2)
print("Anagram check:", are_anagrams("listen", "silent"))

def find_missing_number(lst):
    n = len(lst) + 1  # because one number is missing from the full range
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(lst)
    return expected_sum - actual_sum
print("Missing number:", find_missing_number([1, 2, 3, 5]))

def top_occurring_element(lst):
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    return key_with_max_value(freq)
print("Top occurring element:", top_occurring_element([1, 2, 2, 3, 3, 3, 4]))
