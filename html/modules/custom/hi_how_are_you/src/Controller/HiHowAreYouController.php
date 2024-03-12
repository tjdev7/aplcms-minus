<?php

namespace Drupal\hi_how_are_you\Controller;

use Drupal\Core\Controller\ControllerBase;

class HiHowAreYouController extends ControllerBase {

  public function content() {
    ob_start();
    phpinfo();
    $phpinfo = ob_get_contents();
    ob_end_clean();

    return [
      '#type' => 'markup',
      '#markup' => $this->t('<h2>Hi, how are you?</h2><div>' . $phpinfo . '</div>'),
    ];
  }
  
}