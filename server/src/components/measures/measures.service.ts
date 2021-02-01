import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { CreateMeasureDto } from './dto/create-measure.dto';
import { UpdateMeasureDto } from './dto/update-measure.dto';
import { Measure } from './entities/measure.entity';

@Injectable()
export class MeasuresService {
  constructor(@InjectRepository(Measure) private repo: Repository<Measure>) { }
  async create(createMeasureDto: CreateMeasureDto) {
    return await this.repo.save(createMeasureDto);
  }

  async findAll() {
    return await this.repo.find();
  }

  async findOne(id: number) {
    return await this.repo.findOne(id);
  }

  async update(id: number, updateMeasureDto: UpdateMeasureDto) {
    return await this.repo.update(id, updateMeasureDto);
  }

  async remove(id: number) {
    return await this.repo.delete(id);
  }
}
