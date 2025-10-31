import { Routes } from '@angular/router';
import { ListarTreinamentosComponent } from './components/listar-treinamentos/listar-treinamentos';
import { ListarTurmasComponent } from './components/listar-turmas/listar-turmas';
import { ListarRecursosComponent } from './components/listar-recursos/listar-recursos';
import { CadastroAlunoComponent } from './components/cadastro-aluno/cadastro-aluno';
import { LoginComponent } from './components/login/login';
import { AuthGuard } from './guards/auth.guard';

export const routes: Routes = [
  { path: '', redirectTo: '/login', pathMatch: 'full' }, // rota inicial  
  { path: 'login', component: LoginComponent },
  { path: 'treinamentos', component: ListarTreinamentosComponent, canActivate: [AuthGuard] },
  { path: 'turmas/:treinamentoId', component: ListarTurmasComponent, canActivate: [AuthGuard] },
  { path: '', redirectTo: '/treinamentos', pathMatch: 'full' },
  { path: 'recursos/:turmaId', component: ListarRecursosComponent, canActivate: [AuthGuard] },
  { path: 'alunos', component: CadastroAlunoComponent, canActivate: [AuthGuard] },
  { path: 'turma/:id/recursos', component: ListarRecursosComponent },
];

