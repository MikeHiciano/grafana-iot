import { Module } from '@nestjs/common';
import { MeasuresService } from './measures.service';
import { MeasuresGateway } from './measures.gateway';
import { TypeOrmModule } from '@nestjs/typeorm';
import { Measure } from './entities/measure.entity';

@Module({
  imports: [TypeOrmModule.forFeature([Measure])],
  providers: [MeasuresGateway, MeasuresService],
  exports: [MeasuresService],
})
export class MeasuresModule {}
