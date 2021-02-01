import {
  BaseEntity,
  CreateDateColumn,
  PrimaryGeneratedColumn,
  UpdateDateColumn,
} from 'typeorm';

export abstract class BaseEnt extends BaseEntity {
  @PrimaryGeneratedColumn('increment', { name: 'id' })
  public id: number;

  @CreateDateColumn()
  public createAt: Date;

  @UpdateDateColumn()
  public updateAt: Date;
}
