import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Aluno {
  nome: string; 
  email: string;
  telefone: string;
  password: string;
}

@Injectable({
  providedIn: 'root'
})
export class AlunoService {
  private apiUrl = 'http://localhost:8000/api/alunos/';

  constructor(private http: HttpClient) {}

  cadastrarAluno(data: Aluno): Observable<any> {
    return this.http.post<any>(this.apiUrl, data);
  }

  listarAlunos(): Observable<Aluno[]> {
    return this.http.get<Aluno[]>(this.apiUrl);
  }
}
