import { pgTable, uuid, text, timestamp } from 'drizzle-orm/pg-core';

export const accounts = pgTable('accounts', {
  id: uuid('id').primaryKey(),
  tenantId: uuid('tenant_id').notNull(),
  email: text('email').notNull(),
  createdAt: timestamp('created_at').notNull(),
});
