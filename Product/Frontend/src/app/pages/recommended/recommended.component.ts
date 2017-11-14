import { Component } from '@angular/core';

@Component({
  selector: 'ngx-recommended',
  styleUrls: ['./recommended.component.scss'],
  templateUrl: './recommended.component.html',
})
export class RecommendedComponent {
  modalHeader1 = 'This is where you decide the modal header';
  modalHeader2 = 'this is a different modal so it needs a different variable';
  // Modal content 1-
  modalContent1 = `this is the content that will be shown in the modal`;
  modalContent2 = `same goes for this this is for the second modal`;
}
