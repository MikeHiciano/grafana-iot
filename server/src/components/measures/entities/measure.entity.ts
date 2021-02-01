import { BaseEnt } from '../../../utils/abstracts/entities/base.entity';
import { Column, Entity } from 'typeorm';

@Entity('measures')
export class Measure extends BaseEnt {
  @Column('varchar', { name: 'device', length: 60, nullable: false })
  public device: string;

  @Column('int', { name: 'temperature', nullable: false })
  public temperature: number;

  @Column('int', { name: 'humidity', nullable: false })
  public humidity: number;

  @Column('datetime', { name: 'date', nullable: true })
  public date: Date;
}
