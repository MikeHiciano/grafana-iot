import { Test, TestingModule } from '@nestjs/testing';
import { MeasuresGateway } from './measures.gateway';
import { MeasuresService } from './measures.service';

describe('MeasuresGateway', () => {
  let gateway: MeasuresGateway;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      providers: [MeasuresGateway, MeasuresService],
    }).compile();

    gateway = module.get<MeasuresGateway>(MeasuresGateway);
  });

  it('should be defined', () => {
    expect(gateway).toBeDefined();
  });
});
