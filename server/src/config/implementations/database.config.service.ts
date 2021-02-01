import { Inject, Injectable } from '@nestjs/common';
import { ConfigType } from '@nestjs/config';
import { TypeOrmModuleOptions, TypeOrmOptionsFactory } from '@nestjs/typeorm';
import databaseConfig from '../database.config';

@Injectable()
export class DatabaseConfigService implements TypeOrmOptionsFactory {
  constructor(
    @Inject(databaseConfig.KEY)
    private config: ConfigType<typeof databaseConfig>,
  ) {}

  createTypeOrmOptions(
    connectionName?: string,
  ): Promise<TypeOrmModuleOptions> | TypeOrmModuleOptions {
    return { ...this.config, name: connectionName };
  }
}
