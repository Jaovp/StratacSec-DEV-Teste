import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Matricula {
  id?: number;
  aluno: number;
  turma: number;
  data_matricula?: string;
}

@Injectable({
  providedIn: 'root'
})
export class MatriculaService {
  private apiUrl = 'http://127.0.0.1:8000/api/matriculas/';

  constructor(private http: HttpClient) {}

  criarMatricula(matricula: Matricula): Observable<Matricula> {
    return this.http.post<Matricula>(this.apiUrl, matricula);
  }

  listarMatriculas(): Observable<Matricula[]> {
    return this.http.get<Matricula[]>(this.apiUrl);
  }
}
