import { TestBed } from '@angular/core/testing';

import { Treinamento } from './treinamento';

describe('Treinamento', () => {
  let service: Treinamento;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(Treinamento);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
