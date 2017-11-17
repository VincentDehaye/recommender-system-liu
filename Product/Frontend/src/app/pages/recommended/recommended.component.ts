// Performance page
import { Component } from '@angular/core';

@Component({
  selector: 'ngx-recommended',
  styleUrls: ['./recommended.component.scss'],
  templateUrl: './recommended.component.html',
})
export class RecommendedComponent {
  modalHeader1 = 'Information about success rate over time';
  modalHeader2 = 'Information about the success rate';
  // Modal content 1-
  modalContent1 = `The graph visualised the success progression over time and
                is measured by the overall recommendation success among users.`;
  modalContent2 = `The piechart displayes the latest percentage (presented in green)
                    of successful matches.`;
}
