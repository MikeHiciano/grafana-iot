import { Module } from '@nestjs/common';
import { ConfigModule } from '@nestjs/config';
import { TypeOrmModule } from '@nestjs/typeorm';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { MeasuresModule } from './components/measures/measures.module';
import databaseConfig from './config/database.config';
import { DatabaseConfigService } from './config/implementations/database.config.service';

@Module({
  imports: [
    ConfigModule.forRoot({
      load: [databaseConfig],
    }),
    TypeOrmModule.forRootAsync({
      imports: [ConfigModule.forFeature(databaseConfig)],
      useClass: DatabaseConfigService,
    }),
    MeasuresModule,
  ],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
