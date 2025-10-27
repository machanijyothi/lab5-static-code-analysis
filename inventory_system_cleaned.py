"""
Inventory System Module
Provides a simple stock management tool with logging, persistence,
and validation using JSON storage.
"""

import json
import logging
from datetime import datetime
import ast

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """Add an item to the stock with a given quantity."""
    if logs is None:
        logs = []

    # Input validation
    if not isinstance(item, str) or not isinstance(qty, (int, float)):
        logging.warning("Invalid item or quantity type: %s, %s", item, qty)
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")
    logging.info("Added %s of %s", qty, item)


def remove_item(item, qty):
    """Remove a quantity of an item from the stock."""
    if item not in stock_data:
        logging.warning("Item not found in stock: %s", item)
        return

    stock_data[item] -= qty
    if stock_data[item] <= 0:
        del stock_data[item]
        logging.info("Removed %s completely from stock", item)
    else:
        logging.info("Removed %s of %s", qty, item)


def get_qty(item):
    """Get the current quantity of an item."""
    return stock_data.get(item, 0)


def load_data(file_name="inventory.json"):
    """Load inventory data from a JSON file."""
    global stock_data  # pylint: disable=global-statement
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            stock_data = json.load(f)
        logging.info("Data loaded successfully from %s", file_name)
    except FileNotFoundError:
        logging.warning("File %s not found. Starting with empty inventory.", file_name)
        stock_data = {}
    except json.JSONDecodeError as error:
        logging.error("Error decoding JSON: %s", error)


def save_data(file_name="inventory.json"):
    """Save inventory data to a JSON file."""
    try:
        with open(file_name, "w", encoding="utf-8") as f:
            json.dump(stock_data, f, indent=4)
        logging.info("Data saved successfully to %s", file_name)
    except IOError as error:
        logging.error("Error saving data: %s", error)


def print_data():
    """Display current stock items and quantities."""
    print("\nItems Report:")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold=5):
    """Return a list of items below the given threshold."""
    low_items = [item for item, qty in stock_data.items() if qty < threshold]
    return low_items


def main():
    """Main program for inventory management."""
    add_item("apple", 10)
    add_item("banana", -2)
    add_item("mango", 3)
    remove_item("apple", 3)
    remove_item("orange", 1)

    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")

    save_data()
    load_data()
    print_data()

    # Safe replacement for eval demonstration
    command = "print('eval used')"
    try:
        ast.literal_eval(command)
    except (ValueError, SyntaxError):
        print("Unsafe or invalid command ignored.")


if __name__ == "__main__":
    main()
