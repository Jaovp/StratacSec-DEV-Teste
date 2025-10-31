import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ListarRecursos } from './listar-recursos';

describe('ListarRecursos', () => {
  let component: ListarRecursos;
  let fixture: ComponentFixture<ListarRecursos>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ListarRecursos]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ListarRecursos);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
