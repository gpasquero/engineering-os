import { pgTable, uuid, text, integer, timestamp } from 'drizzle-orm/pg-core';

export const invoices = pgTable('invoices', {
  id: uuid('id').primaryKey(),
  accountId: uuid('account_id').notNull(),
  amountCents: integer('amount_cents').notNull(),
  status: text('status').notNull(),
  issuedAt: timestamp('issued_at').notNull(),
  refundedAt: timestamp('refunded_at'),
});
