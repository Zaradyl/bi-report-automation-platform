"""seed 500 financial transactions

Revision ID: 21baf4003f80
Revises: 08754cc90125
Create Date: 2026-08-23 22:00:54.123051
"""

import random
from datetime import date, timedelta
from decimal import Decimal
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "21baf4003f80"
down_revision: Union[str, Sequence[str], None] = "08754cc90125"
branch_labels = None
depends_on = None


def upgrade() -> None:
    financial_transactions = sa.table(
        "financial_transactions",
        sa.column("transaction_date", sa.Date()),
        sa.column("account", sa.String()),
        sa.column("category", sa.String()),
        sa.column("description", sa.String()),
        sa.column("amount", sa.Numeric(15, 2)),
        sa.column("transaction_type", sa.String()),
    )

    random.seed(42)

    revenue_categories = {
        "Consulting": {
            "min": 150_000,
            "max": 600_000,
            "descriptions": [
                "Client consulting engagement",
                "Business consulting project",
                "Advisory services revenue",
                "Management consulting engagement",
            ],
        },
        "Subscription": {
            "min": 40_000,
            "max": 180_000,
            "descriptions": [
                "Monthly subscription revenue",
                "Annual subscription revenue",
                "Software subscription revenue",
                "Platform subscription revenue",
            ],
        },
        "Professional Services": {
            "min": 75_000,
            "max": 300_000,
            "descriptions": [
                "Implementation services",
                "Technical services engagement",
                "Professional services project",
                "Client implementation revenue",
            ],
        },
        "Other Revenue": {
            "min": 10_000,
            "max": 75_000,
            "descriptions": [
                "Miscellaneous business revenue",
                "Service reimbursement",
                "Other operating revenue",
                "Business service income",
            ],
        },
    }

    expense_categories = {
        "Payroll": {
            "min": 80_000,
            "max": 350_000,
            "descriptions": [
                "Monthly employee payroll",
                "Staff compensation",
                "Payroll expense",
                "Employee salary expense",
            ],
        },
        "Software": {
            "min": 5_000,
            "max": 75_000,
            "descriptions": [
                "Software subscriptions",
                "Cloud software licenses",
                "Technology platform expenses",
                "Business software licenses",
            ],
        },
        "Office": {
            "min": 5_000,
            "max": 50_000,
            "descriptions": [
                "Office supplies",
                "Office operating expenses",
                "Facilities expenses",
                "Office equipment and supplies",
            ],
        },
        "Travel": {
            "min": 5_000,
            "max": 80_000,
            "descriptions": [
                "Business travel",
                "Client travel expenses",
                "Transportation and accommodation",
                "Business trip expenses",
            ],
        },
        "Marketing": {
            "min": 10_000,
            "max": 100_000,
            "descriptions": [
                "Marketing campaign",
                "Digital advertising",
                "Marketing services",
                "Advertising expenses",
            ],
        },
        "Utilities": {
            "min": 5_000,
            "max": 40_000,
            "descriptions": [
                "Electricity and utilities",
                "Internet and telecommunications",
                "Office utilities",
                "Utilities expense",
            ],
        },
        "Professional Fees": {
            "min": 5_000,
            "max": 60_000,
            "descriptions": [
                "Legal and professional fees",
                "Accounting services",
                "Professional consulting fees",
                "External advisory services",
            ],
        },
    }

    # Create 500 transactions distributed across 2025.
    transactions = []

    start_date = date(2025, 1, 1)
    end_date = date(2025, 12, 31)
    days_in_year = (end_date - start_date).days

    # Revenue-heavy distribution makes the dataset useful
    # for P&L and profitability reporting.
    revenue_weight = 0.42
    expense_weight = 0.58

    revenue_count = round(500 * revenue_weight)
    expense_count = 500 - revenue_count

    # Generate revenue transactions.
    revenue_items = list(revenue_categories.items())

    for _ in range(revenue_count):
        category, details = random.choice(revenue_items)

        transaction_date = (
            start_date
            + timedelta(days=random.randint(0, days_in_year))
        )

        amount = Decimal(
            str(
                round(
                    random.uniform(
                        details["min"],
                        details["max"],
                    ),
                    2,
                )
            )
        )

        transactions.append(
            {
                "transaction_date": transaction_date,
                "account": "Revenue",
                "category": category,
                "description": random.choice(
                    details["descriptions"]
                ),
                "amount": amount,
                "transaction_type": "Income",
            }
        )

    # Generate expense transactions.
    expense_items = list(expense_categories.items())

    for _ in range(expense_count):
        category, details = random.choice(expense_items)

        transaction_date = (
            start_date
            + timedelta(days=random.randint(0, days_in_year))
        )

        amount = Decimal(
            str(
                round(
                    random.uniform(
                        details["min"],
                        details["max"],
                    ),
                    2,
                )
            )
        )

        transactions.append(
            {
                "transaction_date": transaction_date,
                "account": "Operating Expenses",
                "category": category,
                "description": random.choice(
                    details["descriptions"]
                ),
                "amount": amount,
                "transaction_type": "Expense",
            }
        )

    # Keep the final dataset ordered chronologically.
    transactions.sort(
        key=lambda transaction: transaction["transaction_date"]
    )

    op.bulk_insert(
        financial_transactions,
        transactions,
    )


def downgrade() -> None:
    financial_transactions = sa.table(
        "financial_transactions",
        sa.column("transaction_date", sa.Date()),
        sa.column("account", sa.String()),
        sa.column("category", sa.String()),
        sa.column("description", sa.String()),
        sa.column("amount", sa.Numeric(15, 2)),
        sa.column("transaction_type", sa.String()),
    )

    # Remove only the sample data created by this migration.
    op.execute(
        sa.delete(financial_transactions)
    )