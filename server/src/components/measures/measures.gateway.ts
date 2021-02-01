import {
  WebSocketGateway,
  SubscribeMessage,
  MessageBody,
} from '@nestjs/websockets';
import { MeasuresService } from './measures.service';
import { CreateMeasureDto } from './dto/create-measure.dto';
import { UpdateMeasureDto } from './dto/update-measure.dto';

@WebSocketGateway()
export class MeasuresGateway {
  constructor(private readonly measuresService: MeasuresService) { }

  @SubscribeMessage('createMeasure')
  create(@MessageBody() createMeasureDto: CreateMeasureDto) {
    return this.measuresService.create(createMeasureDto);
  }

  @SubscribeMessage('findAllMeasures')
  findAll() {
    return this.measuresService.findAll();
  }

  @SubscribeMessage('findOneMeasure')
  findOne(@MessageBody() id: number) {
    return this.measuresService.findOne(id);
  }

  @SubscribeMessage('updateMeasure')
  update(@MessageBody() updateMeasureDto: UpdateMeasureDto) {
    return this.measuresService.update(updateMeasureDto.id, updateMeasureDto);
  }

  @SubscribeMessage('removeMeasure')
  remove(@MessageBody() id: number) {
    return this.measuresService.remove(id);
  }
}
