import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ListarTurmas } from './listar-turmas';

describe('ListarTurmas', () => {
  let component: ListarTurmas;
  let fixture: ComponentFixture<ListarTurmas>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ListarTurmas]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ListarTurmas);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
