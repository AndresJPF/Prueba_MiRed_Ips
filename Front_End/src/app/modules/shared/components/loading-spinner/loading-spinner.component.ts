import { Component } from '@angular/core';

@Component({
  selector: 'app-loading-spinner',
  template: `
    <div class="spinner-container">
      <div class="spinner"></div>
      <p>Cargando...</p>
    </div>
  `,
  styleUrls: ['./loading-spinner.component.css']
})
export class LoadingSpinnerComponent {}
