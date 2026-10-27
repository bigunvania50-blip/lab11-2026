import os

import pandas as pd

# Робочою папкою робимо корінь репозиторію (папку над src),
# щоб шлях data/sales_data.csv працював незалежно від того, звідки запущено програму
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

# ===== Завдання 1: Завантаження та первинний аналіз даних =====
print("===== Завдання 1: Завантаження та первинний аналіз даних =====")
df = pd.read_csv('data/sales_data.csv', parse_dates=['date'])

print("Перші 5 рядків:")
print(df.head())
print("\nОстанні 5 рядків:")
print(df.tail())
print("\nЗагальна інформація:")
df.info()
print("\nСтатистичні характеристики:")
print(df.describe())

# ===== Завдання 2: Фільтрація даних (product_id дорівнює 5 або 10) =====
print("\n===== Завдання 2: Фільтрація даних =====")
filtered_df = df[(df['product_id'] == 5) | (df['product_id'] == 10)]
print(filtered_df)

# ===== Завдання 3: Сортування даних (за order_id, зростання) =====
print("\n===== Завдання 3: Сортування даних =====")
sorted_df = df.sort_values(by='order_id', ascending=True)
print(sorted_df)

# ===== Завдання 4: Групування (за date і store_id, кількість унікальних товарів) =====
print("\n===== Завдання 4: Групування та агрегування даних =====")
grouped_df = df.groupby(['date', 'store_id'])['product_id'].nunique().reset_index(name='unique_products')
print(grouped_df)


# ===== Завдання 5: Додавання стовпця price_category =====
# low: price < 50, medium: 50 <= price <= 100, high: price > 100
def get_price_category(price):
    if pd.isna(price):
        return None  # ціни немає, тому категорію не визначаємо
    elif price < 50:
        return 'low'
    elif price <= 100:
        return 'medium'
    else:
        return 'high'


print("\n===== Завдання 5: Додавання нового стовпця =====")
df['price_category'] = df['price'].apply(get_price_category)
print(df)

# ===== Завдання 6: Видалення стовпців store_id та product_id =====
print("\n===== Завдання 6: Видалення стовпців =====")
df_after_drop = df.drop(columns=['store_id', 'product_id'])
print(df_after_drop)

# ===== Завдання 7: Видалення рядків з пропущеними значеннями =====
print("\n===== Завдання 7: Обробка пропущених значень =====")
print("Кількість пропущених значень у стовпцях:")
print(df_after_drop.isna().sum())
df_clean = df_after_drop.dropna()
print(f"\nРядків до видалення: {len(df_after_drop)}, після видалення: {len(df_clean)}")
print(df_clean)

# ===== Завдання 8: Зведена таблиця (рядки - date, стовпці - price_category, значення - max quantity) =====
print("\n===== Завдання 8: Створення зведеної таблиці =====")
pivot_table = df_clean.pivot_table(values='quantity', index='date', columns='price_category', aggfunc='max')
print(pivot_table)