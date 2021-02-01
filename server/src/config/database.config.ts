import { registerAs } from '@nestjs/config';

export default registerAs('database', () => ({
  name: 'default',
  type: process.env.DATABASE_TYPE as any,
  host: process.env.DATABASE_HOST,
  port: Number(process.env.DATABASE_PORT),
  database: process.env.DATABASE_NAME,
  username: process.env.DATABASE_USERNAME,
  password: process.env.DATABASE_PASSWORD,
  synchronize: Boolean(process.env.DATABASE_SYNCRONIZED),
  migrationsTableName: process.env.DATABASE_MIGRATION_TABLE_NAME,
  entities: [`${__dirname}/../components/**/entities/*.entity{.ts,.js}`],
  migrations: [`${__dirname}/migrations/**/*{.ts,.js}`],
}));
