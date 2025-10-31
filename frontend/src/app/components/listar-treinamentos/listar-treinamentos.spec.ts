import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ListarTreinamentos } from './listar-treinamentos';

describe('ListarTreinamentos', () => {
  let component: ListarTreinamentos;
  let fixture: ComponentFixture<ListarTreinamentos>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ListarTreinamentos]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ListarTreinamentos);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
