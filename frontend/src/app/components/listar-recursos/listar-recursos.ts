import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActivatedRoute } from '@angular/router';
import { RecursoService } from '../../services/recurso';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-listar-recursos',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './listar-recursos.html',
  styleUrls: ['./listar-recursos.scss']
})
export class ListarRecursosComponent implements OnInit {
  recursos: any[] = [];
  turmaId!: number;
  turmaNome = '';
  treinamentoNome = '';
  loading = true;
  error = '';

  showModal = false;
  novoRecurso: any = {
    nome: '',
    tipo_recurso: 'video',
    descricao: '',
    acesso_previo: false,
    draft: true,
    turma: 0
};

tiposRecurso = [
  { value: 'video', label: 'Vídeo' },
  { value: 'pdf', label: 'Arquivo PDF' },
  { value: 'zip', label: 'Arquivo ZIP' }
];

  constructor(private recursoService: RecursoService, private route: ActivatedRoute) {}

  ngOnInit(): void {
    this.turmaId = Number(this.route.snapshot.paramMap.get('turmaId'));
    this.recursoService.listarRecursos(this.turmaId).subscribe({
      next: (data) => {
        this.recursos = data;
        if (data.length > 0) {
          // pegar o nome da turma e do treinamento do primeiro recurso
          this.turmaNome = data[0].turma_nome;
          this.treinamentoNome = data[0].treinamento_nome;
        }
        this.loading = false;
      },
      error: (err) => {
        this.error = 'Erro ao carregar recursos.';
        this.loading = false;
      }
    });
  }

  listarRecursos() {
    this.loading = true;
    this.recursoService.listarRecursos(this.turmaId).subscribe({
      next: (data) => {
        this.recursos = data;
        this.loading = false;
      },
      error: (err) => {
        console.error(err);
        this.error = 'Erro ao carregar recursos.';
        this.loading = false;
      }
    });
  }

  abrirModal() {
    this.novoRecurso = {
      nome: '',
      tipo_recurso: 'video',
      descricao: '',
      acesso_previo: false,
      draft: true,
      turma: this.turmaId
    };
    this.showModal = true;
  }

  fecharModal() {
    this.showModal = false;
  }

  salvarRecurso() {
    this.recursoService.criarRecurso(this.novoRecurso).subscribe({
      next: () => {
        this.fecharModal();
        this.listarRecursos();
      },
      error: (err) => console.error('Erro ao criar recurso:', err)
    });
  }
}
