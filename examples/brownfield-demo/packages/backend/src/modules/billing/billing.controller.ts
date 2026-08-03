import { Controller, Get, Post } from '@nestjs/common';

@Controller('billing')
export class BillingController {
  @Get('invoices')
  list() { return this.service.list(); }

  @Post('invoices')
  create() { return this.service.create(); }

  @Post('invoices/:id/refund')
  refund() { return this.service.refund(); }
}
