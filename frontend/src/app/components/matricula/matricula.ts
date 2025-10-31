import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule, FormsModule } from '@angular/forms';
import { MatriculaService } from '../../services/matricula';
import { AlunoService, Aluno } from '../../services/aluno';
import { TurmaService, Turma } from '../../services/turma';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-matricula',
  templateUrl: './matricula.html',
  styleUrls: ['./matricula.scss'],
  standalone: true,
  imports: [ReactiveFormsModule, FormsModule, CommonModule]
})
export class CadastroMatriculaComponent {

}
