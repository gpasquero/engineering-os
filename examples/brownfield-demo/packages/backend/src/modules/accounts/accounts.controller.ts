import { Controller, Get, Patch } from '@nestjs/common';

@Controller('accounts')
export class AccountsController {
  @Get(':id')
  find() { return this.service.find(); }

  @Patch(':id')
  update() { return this.service.update(); }
}
