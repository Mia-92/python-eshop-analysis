# 📊 Analýza prodejů e-shopu (Python & SQL)

Tento projekt se zaměřuje na zpracování surových exportů z e-shopového systému, jejich čištění a následnou analýzu pomocí databáze **SQLite**. Cílem je transformovat nepřehledná data do smysluplných byznysových statistik.

Výstupy a otázky se mohou v průběhu řešení měnit.

## 🛠️ Technologie a proces
- **Python**: Čištění dat (preprocessing), ošetření nekonzistentních záznamů a import do DB.
- **SQL (sqlite3)**: Architektura databáze a komplexní dotazování pro získání statistik.
- **Data**: Simulované exporty (produkty, zákazníci, objednávky) bez primárních klíčů.

## ❓ Analytické otázky
V rámci projektu se snažím najít odpovědi na následující otázky:

1. **Geografie prodejů**: V jaké oblasti (městě) máme nejvíce zákazníků?
2. **Časová špička**: V jakých dnech a časech se nejvíce prodává (kdy je systém nejvytíženější)?
3. **Audit zákazníků**: Seznam zákazníků s počty jejich dokončených, zrušených a vrácených objednávek včetně celkových útrat.
4. **Bestsellery**: Které produkty jsou hity e-shopu celkově a které dominují v jednotlivých kategoriích?
5. **Kvalita produktů**: Které položky mají nejvyšší míru vratek?
6. **Čisté tržby**: Jaké jsou reálné tržby (bez zrušených a vrácených objednávek)? Kterým kategoriím se daří nejlépe?
7. **Ztracená příležitost**: Kolik peněz tvoří celková hodnota zrušených objednávek?
8. **Rentabilita**: Která kategorie má nejvyšší % marži a která přináší nejvíce peněz v absolutní hodnotě?
9. **Realita po vratkách**: Kolik peněz reálně zbude po odečtení marže u vráceného zboží?

> [!NOTE]  
> Vzhledem ke krátkému časovému období (1 měsíc) a absenci dat o počátečních skladových zásobách není počítána reálná obrátkovost zboží. Projekt se zaměřuje na identifikaci trendů a ziskovosti.

## 📈 Plánované výstupy
Výsledkem analýzy bude sada reportů ve formátu `.csv`:

| Název reportu | Popis |
| :--- | :--- |
| `Top10_produktu.csv` | Přehled nejvýdělečnějších produktů a jejich vratkovost. |
| `Casy_prodeju.csv` | Matice dnů a hodin s počtem objednávek pro plánování marketingu/podpory. |
| `Zakaznicke_objednavky.csv` | Kompletní přehled historie nákupů jednotlivých klientů. |
| `Vratkovost.csv` | Porovnání prodaných vs. vrácených kusů napříč kategoriemi. |
| `Lezaky_vs_Bestsellery.csv` | Identifikace produktů s nulovým prodejem oproti nejprodávanějším. |


