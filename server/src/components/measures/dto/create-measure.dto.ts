import {
  IsDate,
  IsNotEmpty,
  IsNumber,
  IsOptional,
  IsString,
  MaxLength,
} from 'class-validator';

export class CreateMeasureDto {
  @MaxLength(60)
  @IsString()
  @IsNotEmpty()
  public device: string;

  @IsNumber()
  @IsNotEmpty()
  public temperature: number;

  @IsNumber()
  @IsNotEmpty()
  public humidity: number;

  @IsDate()
  @IsOptional()
  public date: Date;
}
