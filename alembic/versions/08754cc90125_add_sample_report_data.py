"""add sample report data

Revision ID: 08754cc90125
Revises: 0106b46230d1
Create Date: 2026-08-23
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "08754cc90125"
down_revision: Union[str, Sequence[str], None] = "0106b46230d1"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "financial_transactions",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column(
            "transaction_date",
            sa.Date(),
            nullable=False,
        ),
        sa.Column(
            "account",
            sa.String(length=100),
            nullable=False,
        ),
        sa.Column(
            "category",
            sa.String(length=100),
            nullable=False,
        ),
        sa.Column(
            "description",
            sa.String(length=255),
            nullable=False,
        ),
        sa.Column(
            "amount",
            sa.Numeric(15, 2),
            nullable=False,
        ),
        sa.Column(
            "transaction_type",
            sa.String(length=50),
            nullable=False,
        ),
    )

    financial_transactions = sa.table(
        "financial_transactions",
        sa.column("transaction_date", sa.Date()),
        sa.column("account", sa.String()),
        sa.column("category", sa.String()),
        sa.column("description", sa.String()),
        sa.column("amount", sa.Numeric(15, 2)),
        sa.column("transaction_type", sa.String()),
    )

    op.bulk_insert(
        financial_transactions,
        [
            # January
            {
                "transaction_date": "2025-01-05",
                "account": "Revenue",
                "category": "Consulting",
                "description": "Client A consulting revenue",
                "amount": 450000.00,
                "transaction_type": "Income",
            },
            {
                "transaction_date": "2025-01-10",
                "account": "Revenue",
                "category": "Subscription",
                "description": "Client subscriptions",
                "amount": 180000.00,
                "transaction_type": "Income",
            },
            {
                "transaction_date": "2025-01-15",
                "account": "Operating Expenses",
                "category": "Payroll",
                "description": "January payroll",
                "amount": 280000.00,
                "transaction_type": "Expense",
            },
            {
                "transaction_date": "2025-01-18",
                "account": "Operating Expenses",
                "category": "Software",
                "description": "Software subscriptions",
                "amount": 35000.00,
                "transaction_type": "Expense",
            },
            {
                "transaction_date": "2025-01-25",
                "account": "Operating Expenses",
                "category": "Office",
                "description": "Office expenses",
                "amount": 45000.00,
                "transaction_type": "Expense",
            },

            # February
            {
                "transaction_date": "2025-02-05",
                "account": "Revenue",
                "category": "Consulting",
                "description": "Client B consulting revenue",
                "amount": 480000.00,
                "transaction_type": "Income",
            },
            {
                "transaction_date": "2025-02-10",
                "account": "Revenue",
                "category": "Subscription",
                "description": "Client subscriptions",
                "amount": 190000.00,
                "transaction_type": "Income",
            },
            {
                "transaction_date": "2025-02-15",
                "account": "Operating Expenses",
                "category": "Payroll",
                "description": "February payroll",
                "amount": 285000.00,
                "transaction_type": "Expense",
            },
            {
                "transaction_date": "2025-02-18",
                "account": "Operating Expenses",
                "category": "Software",
                "description": "Software subscriptions",
                "amount": 36000.00,
                "transaction_type": "Expense",
            },
            {
                "transaction_date": "2025-02-25",
                "account": "Operating Expenses",
                "category": "Office",
                "description": "Office expenses",
                "amount": 46000.00,
                "transaction_type": "Expense",
            },

            # March
            {
                "transaction_date": "2025-03-05",
                "account": "Revenue",
                "category": "Consulting",
                "description": "Client C consulting revenue",
                "amount": 500000.00,
                "transaction_type": "Income",
            },
            {
                "transaction_date": "2025-03-10",
                "account": "Revenue",
                "category": "Subscription",
                "description": "Client subscriptions",
                "amount": 200000.00,
                "transaction_type": "Income",
            },
            {
                "transaction_date": "2025-03-15",
                "account": "Operating Expenses",
                "category": "Payroll",
                "description": "March payroll",
                "amount": 290000.00,
                "transaction_type": "Expense",
            },
            {
                "transaction_date": "2025-03-18",
                "account": "Operating Expenses",
                "category": "Software",
                "description": "Software subscriptions",
                "amount": 37000.00,
                "transaction_type": "Expense",
            },
            {
                "transaction_date": "2025-03-25",
                "account": "Operating Expenses",
                "category": "Office",
                "description": "Office expenses",
                "amount": 47000.00,
                "transaction_type": "Expense",
            },

            # April
            {
                "transaction_date": "2025-04-05",
                "account": "Revenue",
                "category": "Consulting",
                "description": "Client A consulting revenue",
                "amount": 520000.00,
                "transaction_type": "Income",
            },
            {
                "transaction_date": "2025-04-10",
                "account": "Revenue",
                "category": "Subscription",
                "description": "Client subscriptions",
                "amount": 210000.00,
                "transaction_type": "Income",
            },
            {
                "transaction_date": "2025-04-15",
                "account": "Operating Expenses",
                "category": "Payroll",
                "description": "April payroll",
                "amount": 295000.00,
                "transaction_type": "Expense",
            },
            {
                "transaction_date": "2025-04-18",
                "account": "Operating Expenses",
                "category": "Software",
                "description": "Software subscriptions",
                "amount": 38000.00,
                "transaction_type": "Expense",
            },
            {
                "transaction_date": "2025-04-25",
                "account": "Operating Expenses",
                "category": "Office",
                "description": "Office expenses",
                "amount": 48000.00,
                "transaction_type": "Expense",
            },

            # May
            {
                "transaction_date": "2025-05-05",
                "account": "Revenue",
                "category": "Consulting",
                "description": "Client B consulting revenue",
                "amount": 540000.00,
                "transaction_type": "Income",
            },
            {
                "transaction_date": "2025-05-10",
                "account": "Revenue",
                "category": "Subscription",
                "description": "Client subscriptions",
                "amount": 220000.00,
                "transaction_type": "Income",
            },
            {
                "transaction_date": "2025-05-15",
                "account": "Operating Expenses",
                "category": "Payroll",
                "description": "May payroll",
                "amount": 300000.00,
                "transaction_type": "Expense",
            },
            {
                "transaction_date": "2025-05-18",
                "account": "Operating Expenses",
                "category": "Software",
                "description": "Software subscriptions",
                "amount": 39000.00,
                "transaction_type": "Expense",
            },
            {
                "transaction_date": "2025-05-25",
                "account": "Operating Expenses",
                "category": "Office",
                "description": "Office expenses",
                "amount": 49000.00,
                "transaction_type": "Expense",
            },

            # June
            {
                "transaction_date": "2025-06-05",
                "account": "Revenue",
                "category": "Consulting",
                "description": "Client C consulting revenue",
                "amount": 560000.00,
                "transaction_type": "Income",
            },
            {
                "transaction_date": "2025-06-10",
                "account": "Revenue",
                "category": "Subscription",
                "description": "Client subscriptions",
                "amount": 230000.00,
                "transaction_type": "Income",
            },
            {
                "transaction_date": "2025-06-15",
                "account": "Operating Expenses",
                "category": "Payroll",
                "description": "June payroll",
                "amount": 305000.00,
                "transaction_type": "Expense",
            },
            {
                "transaction_date": "2025-06-18",
                "account": "Operating Expenses",
                "category": "Software",
                "description": "Software subscriptions",
                "amount": 40000.00,
                "transaction_type": "Expense",
            },
            {
                "transaction_date": "2025-06-25",
                "account": "Operating Expenses",
                "category": "Office",
                "description": "Office expenses",
                "amount": 50000.00,
                "transaction_type": "Expense",
            },

            # July
            {
                "transaction_date": "2025-07-05",
                "account": "Revenue",
                "category": "Consulting",
                "description": "Client A consulting revenue",
                "amount": 580000.00,
                "transaction_type": "Income",
            },
            {
                "transaction_date": "2025-07-10",
                "account": "Revenue",
                "category": "Subscription",
                "description": "Client subscriptions",
                "amount": 240000.00,
                "transaction_type": "Income",
            },
            {
                "transaction_date": "2025-07-15",
                "account": "Operating Expenses",
                "category": "Payroll",
                "description": "July payroll",
                "amount": 310000.00,
                "transaction_type": "Expense",
            },
            {
                "transaction_date": "2025-07-18",
                "account": "Operating Expenses",
                "category": "Software",
                "description": "Software subscriptions",
                "amount": 41000.00,
                "transaction_type": "Expense",
            },
            {
                "transaction_date": "2025-07-25",
                "account": "Operating Expenses",
                "category": "Office",
                "description": "Office expenses",
                "amount": 51000.00,
                "transaction_type": "Expense",
            },

            # August
            {
                "transaction_date": "2025-08-05",
                "account": "Revenue",
                "category": "Consulting",
                "description": "Client B consulting revenue",
                "amount": 600000.00,
                "transaction_type": "Income",
            },
            {
                "transaction_date": "2025-08-10",
                "account": "Revenue",
                "category": "Subscription",
                "description": "Client subscriptions",
                "amount": 250000.00,
                "transaction_type": "Income",
            },
            {
                "transaction_date": "2025-08-15",
                "account": "Operating Expenses",
                "category": "Payroll",
                "description": "August payroll",
                "amount": 315000.00,
                "transaction_type": "Expense",
            },
            {
                "transaction_date": "2025-08-18",
                "account": "Operating Expenses",
                "category": "Software",
                "description": "Software subscriptions",
                "amount": 42000.00,
                "transaction_type": "Expense",
            },
            {
                "transaction_date": "2025-08-25",
                "account": "Operating Expenses",
                "category": "Office",
                "description": "Office expenses",
                "amount": 52000.00,
                "transaction_type": "Expense",
            },

            # September
            {
                "transaction_date": "2025-09-05",
                "account": "Revenue",
                "category": "Consulting",
                "description": "Client C consulting revenue",
                "amount": 620000.00,
                "transaction_type": "Income",
            },
            {
                "transaction_date": "2025-09-10",
                "account": "Revenue",
                "category": "Subscription",
                "description": "Client subscriptions",
                "amount": 260000.00,
                "transaction_type": "Income",
            },
            {
                "transaction_date": "2025-09-15",
                "account": "Operating Expenses",
                "category": "Payroll",
                "description": "September payroll",
                "amount": 320000.00,
                "transaction_type": "Expense",
            },
            {
                "transaction_date": "2025-09-18",
                "account": "Operating Expenses",
                "category": "Software",
                "description": "Software subscriptions",
                "amount": 43000.00,
                "transaction_type": "Expense",
            },
            {
                "transaction_date": "2025-09-25",
                "account": "Operating Expenses",
                "category": "Office",
                "description": "Office expenses",
                "amount": 53000.00,
                "transaction_type": "Expense",
            },

            # October
            {
                "transaction_date": "2025-10-05",
                "account": "Revenue",
                "category": "Consulting",
                "description": "Client A consulting revenue",
                "amount": 640000.00,
                "transaction_type": "Income",
            },
            {
                "transaction_date": "2025-10-10",
                "account": "Revenue",
                "category": "Subscription",
                "description": "Client subscriptions",
                "amount": 270000.00,
                "transaction_type": "Income",
            },
            {
                "transaction_date": "2025-10-15",
                "account": "Operating Expenses",
                "category": "Payroll",
                "description": "October payroll",
                "amount": 325000.00,
                "transaction_type": "Expense",
            },
            {
                "transaction_date": "2025-10-18",
                "account": "Operating Expenses",
                "category": "Software",
                "description": "Software subscriptions",
                "amount": 44000.00,
                "transaction_type": "Expense",
            },
            {
                "transaction_date": "2025-10-25",
                "account": "Operating Expenses",
                "category": "Office",
                "description": "Office expenses",
                "amount": 54000.00,
                "transaction_type": "Expense",
            },

            # November
            {
                "transaction_date": "2025-11-05",
                "account": "Revenue",
                "category": "Consulting",
                "description": "Client B consulting revenue",
                "amount": 660000.00,
                "transaction_type": "Income",
            },
            {
                "transaction_date": "2025-11-10",
                "account": "Revenue",
                "category": "Subscription",
                "description": "Client subscriptions",
                "amount": 280000.00,
                "transaction_type": "Income",
            },
            {
                "transaction_date": "2025-11-15",
                "account": "Operating Expenses",
                "category": "Payroll",
                "description": "November payroll",
                "amount": 330000.00,
                "transaction_type": "Expense",
            },
            {
                "transaction_date": "2025-11-18",
                "account": "Operating Expenses",
                "category": "Software",
                "description": "Software subscriptions",
                "amount": 45000.00,
                "transaction_type": "Expense",
            },
            {
                "transaction_date": "2025-11-25",
                "account": "Operating Expenses",
                "category": "Office",
                "description": "Office expenses",
                "amount": 55000.00,
                "transaction_type": "Expense",
            },

            # December
            {
                "transaction_date": "2025-12-05",
                "account": "Revenue",
                "category": "Consulting",
                "description": "Client C consulting revenue",
                "amount": 700000.00,
                "transaction_type": "Income",
            },
            {
                "transaction_date": "2025-12-10",
                "account": "Revenue",
                "category": "Subscription",
                "description": "Client subscriptions",
                "amount": 300000.00,
                "transaction_type": "Income",
            },
            {
                "transaction_date": "2025-12-15",
                "account": "Operating Expenses",
                "category": "Payroll",
                "description": "December payroll",
                "amount": 340000.00,
                "transaction_type": "Expense",
            },
            {
                "transaction_date": "2025-12-18",
                "account": "Operating Expenses",
                "category": "Software",
                "description": "Software subscriptions",
                "amount": 46000.00,
                "transaction_type": "Expense",
            },
            {
                "transaction_date": "2025-12-25",
                "account": "Operating Expenses",
                "category": "Office",
                "description": "Office expenses",
                "amount": 60000.00,
                "transaction_type": "Expense",
            },
        ],
    )


def downgrade() -> None:
    op.drop_table("financial_transactions")