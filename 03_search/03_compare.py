import timeit
import boyer_moore_search
import kmp_search
import rabin_karp_search

patterns = ["алгоритм", "такогонеможебути"]

def measure_time(text, pattern):
    bm_time = timeit.timeit(lambda: boyer_moore_search.boyer_moore_search(text, pattern), number=1000)
    kmp_time = timeit.timeit(lambda: kmp_search.kmp_search(text, pattern), number=1000)
    rk_time = timeit.timeit(lambda: rabin_karp_search.rabin_karp_search(text, pattern), number=1000)
    return bm_time, kmp_time, rk_time

# Завантажуємо тексти для пошуку в них
with open('03_search/text_01.txt', 'r', encoding='utf-8') as file1:
    text1 = file1.read()
with open('03_search/text_02.txt', 'r', encoding='utf-8') as file2:
    text2 = file2.read()

# Вимірювання часу для кожного тексту і підрядка
results = {}
for idx, text in enumerate([text1, text2], 1):
    results[f"text_{idx}"] = {}
    for pattern in patterns:
        bm_time, kmp_time, rk_time = measure_time(text, pattern)
        results[f"text_{idx}"][pattern] = {
            "Boyer-Moore": bm_time,
            "Knuth-Morris-Pratt": kmp_time,
            "Rabin-Karp": rk_time,
        }

# Визначення найшвидшого алгоритму
summary = {}
for text_key, pattern_data in results.items():
    summary[text_key] = {}
    for pattern, times in pattern_data.items():
        fastest_algorithm = min(times, key=times.get)
        summary[text_key][pattern] = fastest_algorithm

#Записуємо результати в Markdown 
with open('03_search/03_results.md', 'w', encoding='utf-8') as md_file:
    md_file.write("# Результати порівняння алгоритмів пошуку підрядка\n\n")
    for text_key, pattern_data in results.items():
        md_file.write(f"## {text_key}\n")
        for pattern, times in pattern_data.items():
            md_file.write(f"\n### Підрядок: {pattern}\n")
            for algo, time in times.items():
                md_file.write(f"- {algo}: {time:.6f} секунд\n")
            fastest = summary[text_key][pattern]
            md_file.write(f"\n**Найшвидший алгоритм:** {fastest}\n")
        md_file.write("\n")

    md_file.write("## Загальний висновок\n")
    for pattern in patterns:
        overall_times = {
            "Boyer-Moore": sum(results[f"text_{i}"][pattern]["Boyer-Moore"] for i in range(1, 3)),
            "Knuth-Morris-Pratt": sum(results[f"text_{i}"][pattern]["Knuth-Morris-Pratt"] for i in range(1, 3)),
            "Rabin-Karp": sum(results[f"text_{i}"][pattern]["Rabin-Karp"] for i in range(1, 3)),
        }
        overall_fastest = min(overall_times, key=overall_times.get)
        md_file.write(f"\nДля підрядка '{pattern}' загальний найшвидший алгоритм: **{overall_fastest}**\n")